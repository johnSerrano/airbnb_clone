var webpack = require('webpack'),
    path = require('path');

module.exports = {
    debug: true,
    entry: {
        main: './js/app.js'
    },
    output: {
        path: __dirname,
        filename: './static/bundle.js'
    },
    module: {
        loaders: [{
          test: /\.es6.js$/,
          loader: "babel-loader",
          exclude: /nodes-modules/,
          query: ['es2015', 'react']
        }]
    }
};
