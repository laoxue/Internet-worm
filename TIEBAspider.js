// 加载依赖模块
var http = require('http');
var fs = require('fs');
var cheerio = require('cheerio');
var request = require('request');
var argv = require('yargs').argv;

var url = 'http://tieba.baidu.com/p/5275999259';
// 封装函数
function fezhuangpage(x){
	return startRequest(x);
}
// 主函数
function startRequest(x){
	// http模块获取网页代码
	http.get(x,function(res){
		var html = '';
		var titles = [];
		res.setEncoding('utf-8');
		res.on('data',function(chunk){
				html+=chunk;
		});
		res.on('end',function(){
			// cheerio模块分析html
			var $ = cheerio.load(html);
			var shuzu = []
			for(var i=0;i<$('img[class="BDE_Image"]').length;i++){
				//用node流模式进行下载图片文件
				request($('img[class="BDE_Image"]').eq(i).attr('src')).pipe(fs.createWriteStream('image/'+i+'.png'));
				console.log('正在下载第'+i+'张图片...')
			}

		console.log('下载结束')
		})
	})
}
// 用argv参数让命令行传入参数
fezhuangpage(argv.url); 

//使用方法  命令行 node spider --url 百度贴吧帖子网址(规则是根据百度贴吧结构爬取，所以只支持百度贴吧帖子图片)
