const path = require('path');
const { VueLoaderPlugin } = require('vue-loader');
const BundleTracker = require('webpack-bundle-tracker');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = (env = {}) => {
  return {

    mode: env.prod ? 'production' : 'development',
    devtool: env.prod ? 'source-map' : 'cheap-module-eval-source-map',
    entry: path.resolve(__dirname, './src/main.ts'),
    output: {
      path: path.resolve(__dirname, '../static/dist'),
      publicPath: "/static/",
      filename: "webpack-bundle.js",
      chunkFilename: "[id]-[chunkhash].js"
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
         use: 'file-loader'
       },
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
            filename: "/css/main.css"
        }),
    ],
    devServer: {
      headers: {
        "Access-Control-Allow-Origin":"\*"
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