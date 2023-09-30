
async function getTopData() {
    const response = await fetch('http://127.0.0.1:5000/get-top-data');
    const json = await response.json();
    console.log(json);
}

console.log(1)
getTopData();
