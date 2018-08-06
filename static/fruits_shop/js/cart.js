$(function () {
    Subtotal();
    total_price();
    // 加减点击事件
    $('.change').click(function (e) {
        e.preventDefault();
        var evt = $(e.target);
        var good_id = evt.parent().attr('name');
        var value = evt.parent().find('input').val();
        if (evt.text() == '+'){
            var change_type = 1
        }else if (evt.text() == '-'){
            var change_type = 0
        }
        var data = {'good_id': good_id, 'value': value, 'change_type': change_type};
        $.get('/fruits_shop/change_num/', data, function (data) {
            if (data.code == 200){
                evt.parent().parent().nextAll('.subtotal').text(data.total + '元');
                evt.parent().find('input').val(data.value);
                total_price();
                }
        })
    });
    // 勾选按钮点击事件
    $('.cart_list_td>.col01>input').click(function (evt) {
        var check_status = $(evt.target).prop('checked');
        var cart_id = $(evt.target).attr('name');
        change_status(cart_id, check_status, '', false);
    })
    // 全选按钮点击事件
    $('.settlements>.col01>input').click(function (evt) {
        var all_value = $(evt.target).prop('checked');
        var all_change_status = true;
        change_status('', '', all_value, all_change_status)
    })
});
// 改变状态ajax
function change_status(cart_id='', change_status='', all_value='', all_change_status=false) {
    $.ajax({
        url: '/fruits_shop/change_status/',
        type: 'post',
        headers:{"X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val()},
        dataType: 'json',
        data: {
            'cart_id': cart_id,
            'change_status': change_status,
            'all_change_status': all_change_status,
            'all_value': all_value
        },
        success: function (data) {
            if (data.code == 200){
                if (all_change_status){
                    $('.cart_list_td>.col01>input').prop('checked', all_value)
                }
                total_price()
            }
        },
        error: function (data) {},
    })
}
// 小计ajax函数
function Subtotal() {
    $.get('/fruits_shop/subtotal/',function (data) {
        if (data.code == 200){
            var tmp_list = data.total_list;
            for (var i=0;i<tmp_list.length;i++) {
                var cart_id = tmp_list[i].cart_id
                var total = tmp_list[i].total
                $('#' + cart_id).text(total + '元')
            }
        }
    })
};
// 总价ajax函数
function total_price() {
    $.get('/fruits_shop/total_price/', function (data) {
        if (data.code == 200){
            $('#total').find("em").text(data.total);
            $('#total').find("b").text(data.count);
            $('.total_count').find("em").text(data.all_count)
        }
    })
};

function cart_delete(cart_id) {
    var evt = $(event.target);
    $.get('/fruits_shop/cart_delete/', {'cart_id': cart_id}, function (data) {
        if (data.code==200){
            evt.parents('ul').remove();
            total_price();
            }
    });
};