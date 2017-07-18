
var ExtractTextPlugin = require("extract-text-webpack-plugin");
var path = require('path');

module.exports = {
	entry: './client/_sandbox.js',
	output: {
		path: __dirname,
		filename: './client/static/js/bundle.js'
	},
	devtool: "source-map",
	module: {
		loaders: [
			{
				test: /\.js$/,
				exclude: /(node_modules|bower_components)/,
				loader: 'babel', // 'babel-loader' is also a valid name to reference
				query: {
					presets: ['es2015'],
					comments: false,
				}
			},
			{
				test: /\.sass$/,
				loader: ExtractTextPlugin.extract(
					"style",
					"css?-url!sass" // &minimize
				)
			}

		],
	},
	resolve: {
		alias: {
			'arbuz': path.resolve(__dirname, './client/arbuz'),
			'form': path.resolve(__dirname, './client/form'),
			'part': path.resolve(__dirname, './client/part'),
			'static': path.resolve(__dirname, './client/static'),
		}
	},
	plugins: [
		new ExtractTextPlugin("./client/static/style/app.css")
	]
};