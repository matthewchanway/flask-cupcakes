
async function getAndShowCurrentCupcakes(){

    let res = await axios.get('http://127.0.0.1:5000/api/cupcakes')
    let cupcakes = res.data.cupcakes;
    for(cupcake of cupcakes){
        
        $("#cupcakeList").append(`<li>
        <img src="${cupcake.image}" width="100" height="125">,
        ${cupcake.flavor},
        ${cupcake.size},
        ${cupcake.rating},
        </li>`);
    }
}

getAndShowCurrentCupcakes();

$("#newCupcakeForm").submit(postNewCupcake)


async function postNewCupcake(evt){
    evt.preventDefault();
    let flavor = $("#flavor").val();
    let rating = $("#rating").val();
    let size = $("#size").val();
    let image = $("#image").val();

    console.log(flavor);
    console.log(rating);
    console.log(size);
    console.log(image);
    let newCupcake = {"flavor": `${flavor}`,
                "size": `${size}`,
                "rating": `${rating}`,
                "image": `${image}`}

    await axios.post("http://127.0.0.1:5000/api/cupcakes", newCupcake)
    $("#cupcakeList").empty();
    getAndShowCurrentCupcakes();


}