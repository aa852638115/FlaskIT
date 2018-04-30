/**
 * Created by panxiaohua on 2017/8/16.
 */
$(document).ready(function () {
    init();
    resize();
})

function init() {
    initclick()
    $(window).resize(resize)
    // $('table.datatable').datatable({fixedHeader: true, fixedHeaderOffset: 136});
}

function initclick() {
    $("#leftmenu li.menu").find("a:first").click(function () {
        $(this).parent().toggleClass('li-open')
    })

}

function resize() {
    $('#content').height($(window).height() - 40)
    $('#content .tablediv').height($(window).height() - 120)
}


function toast(msg, type) {
    if (type == undefined) {
        type = 'warning'
    }
    new $.zui.Messager(
        msg,
        {
            icon: 'bell',
            type: type,
            time: 3000,
            close: false
        }).show()
}

function confirmok(msg, callback, ok_label){
    if(ok_label == undefined){
        ok_label = '确定'
    }
    $("#confirmok div.modal-body p").html(msg)
    $("#confirmok_btn").text(ok_label)
    $("#confirmok").modal()
    $('#confirmok_btn').unbind('click')
    $("#confirmok_btn").click(callback)
}

function relocation(url){
    location.href = url
}