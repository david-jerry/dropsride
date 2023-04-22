const glob = require("glob");
const Path = require('path');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

// developer imports
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const WebpackAssetsManifest = require("webpack-assets-manifest");
const CopyWebpackPlugin = require("copy-webpack-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const FaviconsWebpackPlugin = require("favicons-webpack-plugin");
const { InjectManifest } = require('workbox-webpack-plugin');
const Dotenv = require('dotenv-webpack');

const getEntryObject = () => {
  const entries = {};
  glob.sync(Path.join(__dirname, "../dropsride/static/js/app/*.js")).forEach((path) => {
    const name = Path.basename(path, ".js");
    entries[name] = path;
  });
  return entries;
};

module.exports = {
  target: "web",
  context: Path.join(__dirname, '../'),
  entry: getEntryObject,
  output: {
    path: Path.resolve(__dirname, '../dropsride/static/bundles/'),
    publicPath: '/static/',
    filename: 'js/[name]-[fullhash].js',
    chunkFilename: 'js/[name]-[hash].js',
  },
  optimization: {
    splitChunks: {
      chunks: "all",
    },
    runtimeChunk: "single",
  },
  plugins: [
    new Dotenv(
      'systemVars: true'
    ),
    new CleanWebpackPlugin(),
    new CopyWebpackPlugin({
      patterns: [
        { from: Path.resolve(__dirname, "../dropsride/static/vendors"), to: "vendors" },
      ],
    }),
    new WebpackAssetsManifest({
      entrypoints: true,
      output: "manifest.json",
      writeToDisk: true,
      publicPath: true,
    }),
    new BundleTracker({filename: Path.resolve(__dirname, '../webpack-stats.json')}),
    new MiniCssExtractPlugin({ filename: 'css/[name].[contenthash].css' }),
    // for service worker integration
    new FaviconsWebpackPlugin({
      // Your source logo (required)
      logo: Path.resolve(__dirname, "../dropsride/static/vendors/images/favicon/favicon.png"),
      // Prefix path for generated assets
      prefix: "assets/",
      cache: true,
      // manifestRelativePaths: true,
      // Inject the html into the html-webpack-plugin
      appleStatusBarStyle: "black-translucent",
      scope: '/',
      start_url: '/',
      display: 'fullscreen',
      mode: 'webapp',
      devMode: "webapp", // optional can be 'webapp' or 'light' - 'light' by default
      // Favicons configuration options. Read more on: https://github.com/evilebottnawi/favicons#usage
      favicons: {
          appName: "Dropsride", // Your application's name. `string`
          developerName: "Jeremiah E. David",
          developerURL: "http://jeremiahedavid.space",
          background: "#ddd",
          theme_color: "#fff",
          icons: {
              favicons: true, // Create regular favicons. `boolean`
              android: true, // Create Android homescreen icon. `boolean` or `{ offset, background }`
              appleIcon: true, // Create Apple touch icons. `boolean` or `{ offset, background }`
              appleStartup: false, // Create Apple startup images. `boolean` or `{ offset, background }`
              coast: false, // Create Opera Coast icon. `boolean` or `{ offset, background }`
              firefox: true, // Create Firefox OS icons. `boolean` or `{ offset, background }`
              windows: true, // Create Windows 8 tile icons. `boolean` or `{ background }`
              yandex: false, // Create Yandex browser icon. `boolean` or `{ background }`
          },
        },
    }),
    new HtmlWebpackPlugin(),
    new InjectManifest({
      swSrc: Path.resolve(__dirname, '../dropsride/static/js/sw.js'),
      swDest: Path.resolve(__dirname, '../dropsride/static/bundles/sw.js'),
      maximumFileSizeToCacheInBytes: 150000000,
    }),
  ],
  resolve: {
    alias: {
      "~": Path.resolve(__dirname, "../dropsride/static"),
    },
    modules: ['node_modules'],
    extensions: ['.js', '.jsx'],
  },
  module: {
    rules: [
      // we pass the output from babel loader to react-hot loader
      {
        test: /\.mjs$/,
        include: /node_modules/,
        type: "javascript/auto",
      },
      {
        test: /\.html$/i,
        loader: "html-loader",
      },
      {
        test: /\.js$/,
        include: Path.resolve(__dirname, "..dropsride/static/js"),
        loader: 'babel-loader',
      },
      {
        test: /\.s?css$/i,
        use: [
          MiniCssExtractPlugin.loader,
          'css-loader',
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                plugins: [
                  'postcss-preset-env',
                  'autoprefixer',
                  'pixrem',
                  'tailwindcss'
                ],
              },
            },
          },
          'sass-loader',
        ],
      },
      {
        test: /\.(ico|jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2)(\?.*)?$/,
        use: [
          {
            loader: "file-loader",
            options: {
              name: "[path][name].[ext]",
            },
          },
          {
            loader: 'image-webpack-loader',
            options: {
              bypassOnDebug: true,
              compress: {
                // this will take more time and get smaller images
                mode: 'high', // 'lossless', 'low'
                disableOnDevelopment: false,
                // loseless compression for png
                optipng: {
                  optimizationLevel: 4,
                },
                // lossy compression for png. This will generate smaller file than optipng.
                pngquant: {
                  quality: [0.2, 0.8],
                },
                // Compression for webp.
                // You can also tranform jpg/png into webp.
                webp: {
                  quality: 100,
                },
                // Compression for svg.
                svgo: true,
                // Compression for gif.
                gifsicle: {
                  optimizationLevel: 3,
                },
                // Compression for jpg.
                mozjpeg: {
                  progressive: true,
                  quality: 60,
                },
              }
            }
          }
        ]
      },
    ],
  },
};
