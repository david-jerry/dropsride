import axios from "./axiosFactory";
import iziToast from "izitoast/dist/js/iziToast.min.js"; // you have access to iziToast now
import { ethers } from "ethers";
// import Moralis from 'moralis';
// import { env } from 'process';

function sleep(ms) {
  return new window.Promise((resolve) => setTimeout(resolve, ms));
}

export default function ConnectWallet() {
  return {
    address: null,
    user: null,
    chain: null,
    authenticated: false,
    mauthenticated: this.authenticated,
    signature: null,
    balance: 0.00000,
    message: null,
    signer: null,
    csrf: null,
    processing: false,
    provider: null,
    dappServer: null,
    appId: null,
    apiKey: null,

    async init(state) {
      const btn = this.$refs.connectInit;
      this.csrf = btn.dataset.csrf;
      this.dappServer = btn.dataset.server;
      this.appId = btn.dataset.appid;
      this.apiKey = btn.dataset.api;

      this.provider = new ethers.providers.Web3Provider(
        window.ethereum,
        "any"
      );


      if (state) {
        this.authState(state);
      }

      if (this.authenticated === state && state === true) {
        const { signer, chain, account } = await this.connectToMetamask();

        this.signer = signer;
        this.chain = chain;
        this.address = account;

        if (!account) {
          iziToast.error({
            title: "Account Not Found",
            balloon: true,
            position: "topRight",
            animateInside: true,
            message: `we could not connect to your account.`,
          });
        } else {
          iziToast.success({
            title: "Account Connected",
            balloon: true,
            position: "topRight",
            animateInside: true,
            message: `Connected to ${this.address}`,
          });
        }

        if (!chain) {
          iziToast.error({
            title: "Chain Not Found",
            balloon: true,
            position: "topRight",
            animateInside: true,
            message: `we could not connect to your account.`,
          });
        }
        this.balance = await this.provider.getBalance(this.address);
      } else if (this.authenticated === state && state === false) {
        this.handleAuth();
        this.balance = await this.provider.getBalance(this.address);
      }

    },

    authState(state) {
      this.authenticated = state;
    },

    async connectToMetamask() {
      this.processing = true;
      const [accounts, chainId] = await Promise.all([
        this.provider.send("eth_requestAccounts", []),
        this.provider.send("eth_chainId", []),
      ]);

      const signer = this.provider.getSigner();
      return { signer, chain: chainId, account: accounts[0] };
    },

    async requestMessage() {
      const data = {
        address: this.address,
        chain: this.chain,
        network: "evm",
      };

      const reqresponse = await axios.post("/request-message/", data, {
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": this.csrf,
        },
      });
      if (reqresponse.status === 200 && typeof reqresponse === 'object' && reqresponse !== null) {
        iziToast.success({
          title: "Message Request is Successful",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: reqresponse.data,
        });
      } else if (reqresponse.status !== 200 || reqresponse.status !== 201) {
        iziToast.error({
              title: "Message Request has Failed",
              balloon: true,
              position: "topRight",
              animateInside: true,
              message: `Something wrong happened: ${reqresponse.status} \n ${reqresponse.message}`
        });

      }
      return reqresponse.data;
    },

    async verifyMessage() {
      const data = {
        message: this.message,
        signature: this.signature,
        network: "evm",
      };

      const vresponse = await axios.post("/verify-message/", data, {
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": this.csrf,
        },
      });

      if (vresponse.data.user !== null ) {
        iziToast.success({
          title: "Message Verified Successfully",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: vresponse.data,
        });
      } else {
        iziToast.error({
            title: "Message Verification failed",
            balloon: true,
            position: "topRight",
            animateInside: true,
            message: vresponse.data,
          });
      }

      return vresponse.data;
    },

    async handleAuth() {
      // conect to Metamask here
      const { signer, chain, account } = await this.connectToMetamask();

      this.signer = signer;
      this.chain = chain;
      this.address = account;

      if (!account) {
        iziToast.error({
          title: "Account Not Found",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: `we could not connect to your account.`,
        });
      } else {
        iziToast.success({
          title: "Account Connected",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: `Connected to ${this.address}`,
        });
      }

      if (!chain) {
        iziToast.error({
          title: "Chain Not Found",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: `we could not connect to your account.`,
        });
      }

      const { message } = await this.requestMessage();
      this.message = message;

      const signature = await signer.signMessage(message);
      this.signature = signature;

      const { user } = await this.verifyMessage();

      if (user) {
        iziToast.success({
          title: "Authentication Successful",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: `You are authenticated. Do well to add your email to get verified.`,
        });
        sleep(3500);
        this.authenticated = true;
        this.user = user;
      } else {
        iziToast.error({
          title: "Authentication Error",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: `Something went wrong while authenticating you.`,
        });
        this.authenticated = false;
      }

      // if (!this.authenticated) location.reload();
    },

    async getBalance() {
      if(this.authenticated === true) {
        return `${ethers.utils.formatEther(this.balance)} ETH`;
      } else {
        return "0.00000 ETH";
      }
    },

    getBtnText() {
      return this.processing ? "Connecting..." : "Connect Wallet";
    },

    async logoutUser() {

      await window.ethereum.request({method: 'eth_accounts'})[0] || false;

      this.authenticated = false;
      this.processing = false;

      await axios.get("/");
      iziToast.success({
        title: "Account Logged Out Successfully",
        balloon: true,
        position: "topRight",
        animateInside: true,
        message: `thank you for your patronage.`,
      });
      sleep(3500);
      location.reload();
    }
  };
}
