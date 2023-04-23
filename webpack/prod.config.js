const { merge } = require("webpack-merge");
const commonConfig = require("./common.config");
const Webpack = require("webpack");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

// This variable should mirror the one from config/settings/production.py
const staticUrl = "https://dropsride-bucket.s3.amazonaws.com/static/";

module.exports = merge(commonConfig, {
  mode: "production",
  devtool: "source-map",
  bail: true,
  output: {
    publicPath: `${staticUrl}`,
    filename: "js/[name].[chunkhash:8].js",
    chunkFilename: "js/[name].[chunkhash:8].chunk.js",
  },
  plugins: [
    new Webpack.DefinePlugin({
      "process.env.NODE_ENV": JSON.stringify("production"),
    }),
    new MiniCssExtractPlugin({
      filename: "css/[name].[contenthash].css",
    }),
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: "babel-loader",
      },
      {
        test: /\.s?css/i,
        use: [
          MiniCssExtractPlugin.loader,
          "css-loader",
          "postcss-loader",
          "sass-loader",
        ],
      },
    ],
  },
});
