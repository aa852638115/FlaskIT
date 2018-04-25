layui.use('layer')

function toast(msg, type) {
    if (type == undefined) {
        type = 'warning'
    }
    layui.layer.msg(msg, {offset: '50px'})
}