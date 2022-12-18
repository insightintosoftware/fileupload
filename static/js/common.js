const submit = (file) => {
    const chunkSize = 100000;
    const url = 'http://localhost:5070/upload_file';

    let uniqueId = Date.now();
    let chunkLength = Math.ceil(file.size / chunkSize);
    for (let start = 0; start < chunkLength; start++) {
        const chunk = file.slice(start*chunkSize, (start+1)*chunkSize);
        const fd = new FormData();
        fd.append('chunk_id', uniqueId + "_" + pad(start));
        fd.append('chunk_length', chunkLength);
        fd.append('filename', uniqueId);
        fd.append('data', chunk)

        fetch(url, { method: 'post', body: fd }).then(res => console.log(res.text()))
    }
}

const pad = (num) => {
    let zeros = "0000000000"
    let s = zeros + num;
    return s.substr(s.length-zeros.length);
}