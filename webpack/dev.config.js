const Path = require("path");
const Webpack = require("webpack");
const { merge } = require('webpack-merge');
const commonConfig = require('./common.config');
const StylelintPlugin = require("stylelint-webpack-plugin");
const ESLintPlugin = require("eslint-webpack-plugin");

module.exports = merge(commonConfig, {
  mode: 'development',
  devtool: 'inline-source-map',
  devServer: {
    port: 3000,
    proxy: {
      '/': 'http://0.0.0.0:8000',
    },
    headers: {
      "Access-Control-Allow-Origin": "*",
    },
    devMiddleware: {
      writeToDisk: true,
    },
    watchFiles: [
      // Path.join(__dirname, '../portfolio/**/*.py'),
      Path.join(__dirname, '../dropsride/templates/**/*.html'),
    ],
    // We need hot=false (Disable HMR) to set liveReload=true
    hot: false,
    liveReload: true,
  },
  plugins: [
    new Webpack.DefinePlugin({
      "process.env.NODE_ENV": JSON.stringify("development"),
    }),
    new StylelintPlugin({
      files: Path.resolve(__dirname, "../dropsride/static/**/*.s?(a|c)ss"),
    }),
    new ESLintPlugin({
      extensions: "js",
      emitWarning: true,
      files: Path.resolve(__dirname, "../dropsride/static/js"),
    }),
  ],
});
