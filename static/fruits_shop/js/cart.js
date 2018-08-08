
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

 // 把ajax请求的相应传入另一个函数中，由另一个函数处理展示
function show(data) {
    if (data.count){
        $('#show_count').html(data.count);
    }
}
function get_cart_count(func) {
    $.get('/fruits_shop/get_cart_count/', function (json) {
        if (json.code == 200){
            func(json)
        }
    });
}