


//封装ajax
function myAjax( data,url,success) {
    $.ajax({
        type : "get",
        async:true,
        traditional :true,
        data: data,//提交的参数
        url:url,
        dataType : "jsonp",//数据类型为jsonp  
        jsonp: "Callback",//服务端用于接收callback调用的function名的参数  
        success : function(msg){
            console.log(msg)
            success(msg);
            $('.hiddenBtn01').trigger('click')
            $('.hiddenBtn02').trigger('click')
            $('#loadgif').hide()
            $('#floatLayer').hide()//遮罩层
            //未登录用户不可查看详情
            $('.noLogin a').click(function () {
                $('#myModal02').modal({
                    keyboard: true
                })
                return false;
            })
            $("html,body").animate({scrollTop:0}, 0);
            },
        error:function(){
            alert('发生错误，请求数据失败！');
        }
    });
}


//获取url地址问号后面部分
function getQueryStringArgs() {
    var qs= location.search.length > 0 ? location.search.substring(1) : '',
        args = {},
        items = qs.length ? qs.split('&') : [],
        item = null,
        name = null,
        value = null,
        i = 0,
        len = items.length;
    for( i=0;i<len;i++){
        item = items[i].split('=');
        name = decodeURIComponent(item[0]);
        value = decodeURIComponent(item[1]);
        name = item[0];
        value = item[1];

        if (name.length){
            args[name] = value;
        }
    }
    return args;
}

//chrome动态加载JS 代码：
//@ sourceURL=dynamicScript.js
var setPos=function(o){
    if(o.setSelectionRange){//W3C
        setTimeout(function(){
            o.setSelectionRange(o.value.length,o.value.length);
            o.focus();
        },0);
    }else if(o.createTextRange){//IE
        var textRange=o.createTextRange();
        textRange.moveStart("character",o.value.length);
        textRange.moveEnd("character",0);
        textRange.select();
    }
};

//课程点击按钮输入
function Insert(str) {
    var obj = document.getElementById('Course');
    setPos(obj);
    if(document.selection) {
        obj.focus();
        var sel=document.selection.createRange();
        document.selection.empty();
        sel.text = str;
    } else {
        var prefix, main, suffix;
        prefix = obj.value.substring(0, obj.selectionStart);
        main = obj.value.substring(obj.selectionStart, obj.selectionEnd);
        suffix = obj.value.substring(obj.selectionEnd);
        obj.value = prefix + str + suffix;
    }
    obj.focus();
}

//国际课程认证 点击按钮输入
function Insert01(str) {
    var obj = document.getElementById('Authentication');
    setPos(obj);
    if(document.selection) {
        obj.focus();
        var sel=document.selection.createRange();
        document.selection.empty();
        sel.text = str;
    } else {
        var prefix, main, suffix;
        prefix = obj.value.substring(0, obj.selectionStart);
        main = obj.value.substring(obj.selectionStart, obj.selectionEnd);
        suffix = obj.value.substring(obj.selectionEnd);
        obj.value = prefix + str + suffix;
    }
    obj.focus();
}

//学制点击按钮输入
function Insert02(str) {
    var obj = document.getElementById('School_system');
    setPos(obj);
    if(document.selection) {
        obj.focus();
        var sel=document.selection.createRange();
        document.selection.empty();
        sel.text = str;
    } else {
        var prefix, main, suffix;
        prefix = obj.value.substring(0, obj.selectionStart);
        main = obj.value.substring(obj.selectionStart, obj.selectionEnd);
        suffix = obj.value.substring(obj.selectionEnd);
        obj.value = prefix + str + suffix;
    }
    obj.focus();
}

//参加外部考试与评估 点击按钮输入
function Insert03(str) {
    var obj = document.getElementById('Course_evaluation');
    setPos(obj);
    if(document.selection) {
        obj.focus();
        var sel=document.selection.createRange();
        document.selection.empty();
        sel.text = str;
    } else {
        var prefix, main, suffix;
        prefix = obj.value.substring(0, obj.selectionStart);
        main = obj.value.substring(obj.selectionStart, obj.selectionEnd);
        suffix = obj.value.substring(obj.selectionEnd);
        obj.value = prefix + str + suffix;
    }
    obj.focus();
}


//删除一条信息
function ConfirmDelete(){
    var x;
    var args =getQueryStringArgs();
    var schoolId = decodeURIComponent(args['School_name'])
    var r=confirm("确定要删除本条记录吗？");
    if (r==true){
        $.ajax({
            type : "get",
            async:false,
            traditional :true,
            data: {
                'Id': schoolId
            },//提交的参数
            url:'http://'+changeUrl.address+'/School_api?whereFrom=delete',
            dataType : "jsonp",//数据类型为jsonp  
            jsonp: "Callback",//服务端用于接收callback调用的function名的参数  
            success : function(msg){
                alert('删除成功')
                console.log(msg)
                if(msg.msg == 1){
                    window.location.href ='./search.html'
                }
            },
            error:function(){
                alert('发生错误，请求数据失败！');
            }
        });
    }
    else{
        x="你按下了\"取消\"按钮!";
    }
}

//亩米转换器
function Mu2Meter(){
    var Mu=document.getElementById("Mu2MeterID");
    var Mu=Mu.value;
    var Meter=Mu*666;
    var MeterInner = document.getElementById("Meter2MuID");
    MeterInner.value = Meter;
}
function Meter2Mu(){
    var Meter=document.getElementById("Meter2MuID");
    var Meter=Meter.value;
    var Mu=parseInt(Meter/666);
    var MuInner = document.getElementById("Mu2MeterID");
    MuInner.value = Mu;
}

//除去搜索页面的获取cookie
function getCookie() {
    $(function () {
        $.ajax({
            type : "get",
            async:true,
            traditional :true,
            data: {
                'member_sign':$.cookie('usertitle'),
                'username':$.cookie('username'),
                'UserVerifyCode':$.cookie('userVerifyCode')
            },//提交的参数
            url:'http://'+changeUrl.address+'/User_api?whereFrom=verify',
            dataType : "jsonp",//数据类型为jsonp  
            jsonp: "Callback",//服务端用于接收callback调用的function名的参数  
            success : function(msg){
                // alert('成功')
                console.log(msg.verifyResult);
                if(msg.verifyResult<0){
                    alert('当前用户未登录，无法访问该页面')
                    window.location.href="../user/login.html"   //未登录，跳回登录页面
                    console.log($.cookie('usertitle'))
                    console.log($.cookie('username'))
                    console.log($.cookie('userVerifyCode'))
                    console.log( $.cookie('User_TureName'))
                }else{
                    $('.loginUser').text( $.cookie('User_TureName'))
                }
            },
            error:function(){
                alert('发生错误，请求数据失败！');
            }
        });
    })
}

//退出登录，删除cookie
function exitLogin() {
    $.cookie('usertitle', null , { expires: -1, path: '/'  });
    $.cookie('username',null , { expires: -1 ,path: '/'});
    $.cookie('User_TureName', null , { expires: -1 ,path: '/'});
    $.cookie('userVerifyCode', null , { expires: -1 ,path: '/'});
    window.location.href = '../user/login.html'
}

//退回登录删除cookie
$('#exitLogin02').click(function () {
    exitLogin()
})

//返回顶部
$(function () {
    $('#backToTop').hide()
    $(window).scroll(function () {
        if($(this).scrollTop()>54){
            $('#backToTop').fadeIn()
        }else {
            $('#backToTop').fadeOut()
        }
    })
    $('#backToTop').click(function () {
        $('html , body').animate({scrollTop: 0},'slow');
    })
})

//用户等级显示
$(function () {
    $('#userLevel').text('Lv'+$.cookie('usertitle'))
})

//导航条登录状态显示
$(function () {
    var username =  $.cookie('User_TureName')
    if( username == undefined) {
        $('.rightNav li').eq(1).css('display','block')
        $('.rightNav li').eq(2).css('display','block')
        $('.rightNav li').eq(3).css('display','none')
        $('.rightNav li').eq(4).css('display','none')
    }else{
        $('.loginUser').text(username)
    }
})

//过滤函数（如果为零，自动补暂无）
function zeroToEmpty( str ) {
    var strFilter = null;
    return strFilter = (str == 0)? '  ' : str;
}

//判断是否移动端，如果是则跳转到指定的URL地址
function browserRedirect(url) {
//只读的字符串，声明了浏览器用于 HTTP 请求的用户代理头的值
    var sUserAgent = navigator.userAgent.toLowerCase();
    var bIsIphoneOs = sUserAgent.match(/iphone os/i) == "iphone os";
    var bIsMidp = sUserAgent.match(/midp/i) == "midp";
    var bIsUc7 = sUserAgent.match(/rv:1.2.3.4/i) == "rv:1.2.3.4";
    var bIsUc = sUserAgent.match(/ucweb/i) == "ucweb";
    var bIsAndroid = sUserAgent.match(/android/i) == "android";
    var bIsCE = sUserAgent.match(/windows ce/i) == "windows ce";
    var bIsWM = sUserAgent.match(/windows mobile/i) == "windows mobile";
    if (bIsIphoneOs || bIsMidp || bIsUc7 || bIsUc || bIsAndroid || bIsCE || bIsWM) {
        window.location.replace(url);
    }
}
browserRedirect('http://data.xinxueshuo.cn/wap')


