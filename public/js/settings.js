file_list = [];
$.get('public/data/file_list.txt', (data) => {
    file_list = data.split("\n");
});