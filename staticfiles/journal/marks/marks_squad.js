$(document).ready(function () {
    let marksTable = $('#marks')
        .DataTable({
            paging: false,
            lengthChange: false,
            searching: false,
            ordering: false,
        })
        .on('edit', 'tbody td', function () {
            console.log('value by API : ', this.parentNode.rowIndex, this.cellIndex, this.textContent);
        });

    $(".mycell")
        .inputFilter(function (value) {
            return ["1", "2", "3", "4", "5", "Н", "н", "У", "у", ""].includes(value);
        })
        .change(function () {
            let s = ('' + this.name).replace(/'/g, '"');
            s = JSON.parse(s);
            let val = {
                x_index: s.x_index,
                y_key_id: s.y_key_id,
            };
            console.log('val: ', this.value, val.x_index, val.y_key_id);
            let x = get_x_key(val.x_index);
            console.log('x=', x);
            let y = get_y_key(val.y_key_id);
            console.log('y=', y);
        });

    console.log(x_keys);
    console.log(y_keys);

    function get_x_key(x_index) {
        return x_keys[-1 + x_index]
    }

    function get_y_key(y_key_id) {
        return y_keys.filter(y => (y.id === y_key_id))[0]
    }
});
