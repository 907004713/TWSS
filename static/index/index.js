$(document).ready(function () {

    var warnings = $('#warnings');
    var username = $('#username');
    var password = $('#password');

    var captcha = $('#captcha');
    var captcha_img = $('#captcha_img');

    // 禁用双击选择文字
    captcha_img.addClass('no_select');

    var captcha_generate;
    var dict = ['0','1','2','3','4','5','6','7','8','9',
        '0','1','2','3','4','5','6','7','8','9',
        '0','1','2','3','4','5','6','7','8','9',
        '0','1','2','3','4','5','6','7','8','9',
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M',
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];

    // 验证码生成函数
    function init_captcha() {
        captcha_generate = '';
        for(var i = 0; i < 4; i++){
            var rand = Math.floor(Math.random()*92);
            captcha_generate += dict[rand];
        }
        //显示验证码
        captcha_img.text(captcha_generate);
    }
    // 生成验证码
    init_captcha();

    // 点击验证码切换
    captcha_img.click(function () {
        // 清空验证码输入框
        // 延迟0.3秒
        setTimeout(function () {
            captcha.val('').focus();
            init_captcha();
        },300);
    });

    // 输完验证码按回车 模拟点击登录按钮
    captcha.bind('keydown',function (event) {
       if(event.keyCode == '13'){
           $('#login').trigger('click');
       }
    });
    

    // 点击登录
    $('#login').click(function () {

        // 测试开关
        // 跳过验证码
        var PROJECT_TEST = true;
        if(PROJECT_TEST){
            $('#login_form').submit();
        }


        // 检查账户名密码是否为空
        if(username.val() === ''){
            warnings.text('用户名不能为空');
            return -1;
        }
        if(password.val() === ''){
            warnings.text('密码不能为空');
            return -2;
        }

        // 校验验证码
        var captcha_input = captcha.val();
        if( captcha_input !== captcha_generate &&
            captcha_input !== captcha_generate.toLowerCase() &&
            captcha_input !== captcha_generate.toUpperCase())  {
            warnings.text('验证码错误');
            //刷新验证码
            captcha_img.trigger('click');
            return -3;
        }

        // md5加密密码
        password.val(hex_md5(password.val()));
        // 提交
        $('#login_form').submit();


    });


    
});