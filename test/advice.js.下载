//advice 弹窗
$(function() {
    var bg = $("#bg"),
        adviceBox = $("#adviceBox"),
        closeadviceBox = $("#closeadviceBox"),
        footerSec = $("#footer-sec"),
        advice = $("#advice").children('a'),
        send = $("#send"),
        windowWidth = $(window).width(),
        windowHeight = $(window).height()

    adviceBox.click(function(event) {
            event.stopPropagation();
        })
        // 展示
    $("#advice a,#feedback").click(function() {
            // footerSec.css("padding", 0)
            adviceBox.removeClass("flipOutY").addClass("flipInY")
            bg.fadeIn(100)
            send.click(function() {
                var checkboxVal = "",
                    adviceVal = $("#adviceArea").val(),
                    connectVal = $("#connect").val(),
                    username = $.cookie('username') == undefined ? 'undefinedUser' : $.cookie('username')
                $("input[name='qusetion']:checked").each(function() {
                    checkboxVal += $(this).val() + ";"
                })
                $.ajax({
                    type: "POST",
                    url: 'http://' + changeUrl.address + '/User_api?whereFrom=feedback',
                    dataType :   "jsonp", //数据类型为jsonp  
                    jsonp:   "Callback", //服务端用于接收callback调用的function名的参数 
                    data: {
                        'UserName': username,
                        'content': checkboxVal + adviceVal,
                        'Contact': connectVal
                    }, //提交的参数
                    success: function(msg) {
                        layer.msg("反馈成功，我们将会及时通知您问题处理的进展")
                        adviceBox.removeClass("flipInY").addClass("flipOutY")
                        bg.fadeOut(1000)
                    },
                    error: function() {
                        layer.msg("发生错误，服务器异常！请稍后尝试")
                        adviceBox.removeClass("flipInY").addClass("flipOutY")
                        bg.fadeOut(1000)
                    }
                })
            })
        })
        // 影藏

    window.onload=function(){
        $("#bg").height($(document).height())
    }
    bg.click(function() {
        footerSec.css("padding", "30px 0")
        adviceBox.removeClass("flipInY").addClass("flipOutY")
        bg.fadeOut(1000)
    })
    closeadviceBox.click(function() {
        footerSec.css("padding", "30px 0")
        adviceBox.removeClass("flipInY").addClass("flipOutY")
        bg.fadeOut(1000)
    })
})