// 获取cookie
var args = getQueryStringArgs();
var datailSchool = decodeURIComponent(args['School_name'])

//过滤函数（如果为零，自动补空，地址用）
function zeroToAddress(str) {
    var strFilter = null;
    return strFilter = (str == 0) ? '' : str;
}

//过滤函数“其他”
function filter(str) {
    var result = null;
    return result = (str == "其他") ? '' : str
}



$(function() {
    getCookie();
    $.ajax({
        type: "get",
        async: false,
        traditional: true,
        data: {
            'Id': datailSchool
        }, //提交的参数
        url: 'http://' + changeUrl.address + '/School_api?whereFrom=detail',
        dataType :   "jsonp", //数据类型为jsonp  
        jsonp:   "Callback", //服务端用于接收callback调用的function名的参数  
        success :   function(msg) {
            console.log(msg)
            var imgSrc = msg[0].School_logo ? 'http://' + changeUrl.imgAddress + msg[0].School_logo : '../assets/img/schoolNoPic.png';
            $('#School_logo').attr('src', imgSrc)
            $('#School_name').text(zeroToEmpty(msg[0].School_name))
            $('#School_EnglishName').text(zeroToEmpty(msg[0].School_EnglishName))
            $('#School_properties').text(zeroToEmpty(msg[0].School_properties))
            $('#OperationState').text(zeroToEmpty(msg[0].OperationState))

            // $('#Areas').text(filter(msg[0].Areas))
            // $('#Areas02').text(filter(msg[0].Areas02))
            // $('#Areas03').text(zeroToAddress(msg[0].Areas03))
            $('#Address').text(filter(msg[0].Areas) + " " + filter(msg[0].Areas02) + " " + zeroToAddress(msg[0].Areas03))
            $('#Website').text(zeroToEmpty(msg[0].Website))
            $('#Website').attr("href", "http://" + zeroToEmpty(msg[0].Website))
            $('#Telephone').text(zeroToEmpty(msg[0].Telephone))
            $('#School_system').text(zeroToEmpty(msg[0].School_system))
            $('#Founded_time').text(zeroToEmpty(msg[0].Founded_time))
            $('#TuitionHigh').text(zeroToEmpty(msg[0].TuitionHigh))

            $('#Tuition01').text(zeroToEmpty(msg[0].Tuition01))
            $('#Tuition02').text(zeroToEmpty(msg[0].Tuition02))
            $('#Tuition03').text(zeroToEmpty(msg[0].Tuition03))
            $('#Tuition04').text(zeroToEmpty(msg[0].Tuition04))

            $('#Inter_Course_Founded_time').text(zeroToEmpty(msg[0].Inter_Course_Founded_time))
            $('#Club_Num').text(zeroToEmpty(msg[0].Club_Num))
            $('#Course_evaluation').text(zeroToEmpty(msg[0].Course_evaluation))
            $('#Stu_Year_Investment').text(zeroToEmpty(msg[0].Stu_Year_Investment))
            $('#Course').text(zeroToEmpty(msg[0].Course))
            $('#Student_Capacity').text(zeroToEmpty(msg[0].Student_Capacity))
            $('#Authentication').text(zeroToEmpty(msg[0].Authentication))
            $('#Graduated_Stu_Num').text(zeroToEmpty(msg[0].Graduated_Stu_Num))
            $('#Stu_Dominant_nationality').text(zeroToEmpty(msg[0].Stu_Dominant_nationality))
            $('#Student_Num_All').text(zeroToEmpty(msg[0].Student_Num_All))

            $('#Student_Num01').text(zeroToEmpty(msg[0].Student_Num01))
            $('#Student_Num02').text(zeroToEmpty(msg[0].Student_Num02))
            $('#Student_Num03').text(zeroToEmpty(msg[0].Student_Num03))
            $('#Student_Num04').text(zeroToEmpty(msg[0].Student_Num04))

            $('#President_Country').text(zeroToEmpty(msg[0].President_Country))
            $('#Staff_Num').text(zeroToEmpty(msg[0].Staff_Num))
            $('#Teacher_Salary').text(zeroToEmpty(msg[0].Teacher_Salary))
            $('#Teacher_Num').text(zeroToEmpty(msg[0].Teacher_Num))
            $('#Teacher_Year_Investment').text(zeroToEmpty(msg[0].Teacher_Year_Investment))
            $('#Foreign_Teacher_num').text(zeroToEmpty(msg[0].Foreign_Teacher_num))
            $('#Teacher_Stu_ratio').text(zeroToEmpty(msg[0].Teacher_Stu_ratio))
            $('#Teacher_Retention').text(zeroToEmpty(msg[0].Teacher_Retention))

            $('#Covered_Area').text(zeroToEmpty(msg[0].Covered_Area))
            $('#Built_Area').text(zeroToEmpty(msg[0].Built_Area))
            $('#Hardware').text(zeroToEmpty(msg[0].Hardware))
            $('#Investment').text(zeroToEmpty(msg[0].Investment))
            $('#Remark').text(zeroToEmpty(msg[0].Remark))

            $('#Load_People').text(msg[0].Load_People)
            $('#Load_Time').text(msg[0].Load_Time)

            // 学校名
            $('.schoolName').text(msg[0].School_name)
                //学校网址(先判断是否只有http或https)
                // website = msg[0].Website.substr(0,7).toLowerCase() == "http://" ? msg[0].Website : "http://" + msg[0].Website;

            if (msg[0].Website.substr(0, 7).toLowerCase() == "http://") {
                website = msg[0].Website
            } else if (msg[0].Website.substr(0, 7).toLowerCase() == "https:/") {
                website = msg[0].Website
            } else {
                website = "http://" + msg[0].Website;
            }
            $('.Website').attr('href', website)

            //学校ID
            $('.everySchoolID').val(msg[0].Id)
            $('.headerSchoolID').text(msg[0].Id)
            accsessControl()

            // 硬件设施
            var Hardware = $("#Hardware")
            Hardware.siblings().height(Hardware.height()).css('lineHeight', Hardware.height() + "px")
                // 备注
            var Remark = $("#Remark")
            Remark.siblings().height(Remark.height()).css('lineHeight', Remark.height() + "px")
        },
        error: function() {
            alert('发生错误，请求数据失败！');
        }
    });

})

//点击显示图片上传模态框（自制）
$('#upHeadImg').click(function() {
    $('#upImgModal').animate({
        top: 100
    }, 500)
    $('#modalBg').css({ 'background': 'rgba(153,153,153,.8)', 'position': 'fixed', 'z-index': 5 })
    uploadIMG() //图片上传
})
$('#closeUpImg').click(function() {
    $('#upImgModal').animate({
        top: -500
    }, 500)
    $('#modalBg').css({ 'background': '', 'position': '', 'z-index': '' })
})



// 权限管理
function accsessControl() {
    console.log($.cookie('usertitle'))
    var num = $.cookie('usertitle');
    if (num == undefined) {
        //导航条登录显示控制
        //   alert(-2)
        $('.rightNav li').eq(0).css('display', 'block')
        $('.rightNav li').eq(1).css('display', 'block')
        $('.rightNav li').eq(2).css('display', 'none')
        $('.rightNav li').eq(3).css('display', 'none')
            //详情页面删除按钮
        $('#deleteDetail').click(function() {
                $('#myModal').modal({
                    keyboard: true
                })
            })
            //详情页面修改按钮
        $('#modifyDetail').click(function() {
            $('#myModal').modal({
                keyboard: true
            })
        })
    } else if (num == 1) {
        //详情页面删除按钮
        $('#deleteDetail').click(function() {
                $('#myModal').modal({
                    keyboard: true
                })
            })
            //详情页面修改按钮
        $('#modifyDetail').click(function() {
            $('#myModal').modal({
                keyboard: true
            })
        })
        $('#Inter_Course_Founded_time,#Student_Num01,#Student_Num02,#Student_Num03,#Student_Num04,#Authentication,#Course_evaluation,#Student_Num_All,#Student_Capacity,#Graduated_Stu_Num,#Stu_Dominant_nationality,#Stu_Year_Investment,#Club_Num,#President_Country,#Staff_Num,#Teacher_Num,#Foreign_Teacher_num,#Teacher_Year_Investment,#Teacher_Retention,#Teacher_Salary,#Teacher_Stu_ratio,#Covered_Area,#Built_Area,#Investment,#Remark').text('权限不足').css({ 'color': '#CCCCCC', 'fontSize': '14px' })
    } else if (num == 2) {
        //详情页面删除按钮
        $('#deleteDetail').click(function() {
                $('#myModal').modal({
                    keyboard: true
                })
            })
            //详情页面修改按钮
        $('#modifyDetail').click(function() {
            $('#myModal').modal({
                keyboard: true
            })
        })
        $('#Teacher_Num,#Student_Capacity,#Stu_Year_Investment,#Foreign_Teacher_num,#Teacher_Year_Investment,#Teacher_Retention,#Teacher_Salary,#Investment,#Remark').text('权限不足').css({ 'color': '#CCCCCC', 'fontSize': '14px' })

    } else if (num == 3) {
        //详情页面删除按钮
        $('#deleteDetail').click(function() {
                $('#myModal').modal({
                    keyboard: true
                })
            })
            //详情页面修改按钮
        $('#modifyDetail').click(function() {
            $('#myModal').modal({
                keyboard: true
            })
        })
        $('#Investment').text('权限不足').css({ 'color': '#CCCCCC', 'fontSize': '14px' })
    } else {
        //详情页面删除按钮
        $('#deleteDetail').click(function() {
                ConfirmDelete();
            })
            //修改
        $('#modifyDetail').click(function() {
            window.location.href = './alert.html?School_name=' + datailSchool
        })
    }
}