const webpack = require('webpack');
const path = require('path');

module.exports = {
    // entry: './js/entry.js',
    entry: ['./js/camera.js','./js/demo_util.js'],
    output: {
        path: path.resolve(__dirname, 'dist'),
        publicPath: '/dist/',
        filename: 'bundle.js',
        sourceMapFilename: "version.js.map"
    },
    devtool: "source-map",
    module: {
        rules: [
            {
                test: /\.js$/,
                include: path.join(__dirname),
                exclude: /(node_modules)|(dist)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['@babel/preset-env']
                    }
                }
            }
        ]
    }
};