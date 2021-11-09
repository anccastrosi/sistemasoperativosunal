
const path = require ("path")

module.exports = {
   entry: './src/index.js',
    output: {
        filename: 'main.js',
        path:path.join(__dirname,'./dist'),
    },
    devServer:{
        path:path.resolve(__dirname,'./dist'),
        port:9000,
        compress:true,
    },
}