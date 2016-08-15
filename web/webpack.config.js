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
          test: /\.(js|jsx)?$/,
          loader: "babel",
          exclude: /nodes-modules/,
          query: {
            presets: ['es2015', 'react']
          }
        }]
    }
};
