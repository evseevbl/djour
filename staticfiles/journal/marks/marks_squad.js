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
                mark_id: s.mark_id,
            };
            // console.log('val: ', this.value, val.x_index, val.y_key_id);
            let x = get_x_key(val.x_index);
            let y = get_y_key(val.y_key_id);
            let m = make_mark(x, y, subject_id, val.mark_id, this.value);
            // console.log(m);

            axios
                .post('/api/marks/add', m)
                .then((response) => console.log(response));
        });

    function get_x_key(x_index) {
        return x_keys[-1 + x_index]
    }

    function get_y_key(y_key_id) {
        return y_keys.filter(y => (y.id === y_key_id))[0]
    }

    function make_mark(x, y, subject_id, mark_id, val) {
        if (mark_id === '') {
            mark_id = null;
        } else {
            mark_id = parseInt(mark_id, 10);
        }
        return {
            date: x.val,
            student_id: y.val,
            subject_id: subject_id,
            mark_id: mark_id,
            value: val,
        }
    }
});
