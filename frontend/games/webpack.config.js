const path = require('path');
const {VueLoaderPlugin} = require('vue-loader');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const webpack = require('webpack');

module.exports = (env = {}) => {
  return {

    mode: env.prod ? 'production' : 'development',
    devtool: env.prod ? false : "eval",
    entry: path.resolve(__dirname, './src/main.ts'),
    output: {
      path: path.resolve(__dirname, '../static/dist'),
      publicPath: "/static/",
      filename: "webpack-bundle.js",
      chunkFilename: "[id]-[chunkhash].js",
      hotUpdateChunkFilename: "hot-update/hot-update.js",
      hotUpdateMainFilename: "hot-update/hot-update.json"
    },
    module: {
      rules: [
        {
          test: /\.vue$/,
          use: 'vue-loader'
        },
        {
          test: /\.ts$/,
          loader: 'ts-loader',
          options: {
            appendTsSuffixTo: [/\.vue$/],
          }
        },
        {
          test: /\.css$/,
          use: [
            'vue-style-loader',
            {
              loader: 'css-loader',
              options: {
                // enable CSS Modules
                modules: true,
              }
            }
          ]
        },
        {
          test: /\.scss$/,
          use: [
            MiniCssExtractPlugin.loader,
            {
              loader: 'css-loader',
            },
            {
              loader: 'sass-loader',
              options: {
                sourceMap: true,
              }
            }
          ]

        },
        {
          test: /\.(png|svg|jpg|gif)$/,
          use: 'asset/resource'
        },
        {
          test: /\.m?js$/,
          exclude: /(node_modules|bower_components)/,
          use: {
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-env'],
              plugins: ["@babel/plugin-proposal-class-properties"],
            }
          }
        }
      ]
    },
    resolve: {
      extensions: ['.ts', '.js', '.vue', '.json'],
      alias: {
        'vue': '@vue/runtime-dom'
      }
    },
    plugins: [
      new VueLoaderPlugin(),
      new BundleTracker({
        filename: './webpack-stats.json',
        publicPath: 'http://0.0.0.0:8080/'
      }),
      new MiniCssExtractPlugin({
        filename: "css/main.css"
      }),
      new webpack.DefinePlugin({
        __VUE_OPTIONS_API__: JSON.stringify(true),
        __VUE_PROD_DEVTOOLS__: JSON.stringify(false),
      }),
    ],
    devServer: {
      headers: {
        "Access-Control-Allow-Origin": "\*"
      },
      public: 'http://0.0.0.0:8080',
      inline: true,
      hot: true,
      stats: "minimal",
      contentBase: __dirname,
      overlay: true,
      writeToDisk: true, // Write files to disk in dev mode, so Django can serve the assets
    }
  };
}
