const products = document.querySelector("#products");

let cart = JSON.parse(localStorage.getItem("cart")) || [];

const getAllProducts = async () => {
    try {
        const response = await fetch("https://dummyjson.com/products");
        const data = await response.json();

        data.products.forEach(product => {
            const div = document.createElement("div");

            const productBtn = document.createElement("button");
            productBtn.textContent = "Add to Cart";
            
            div.innerHTML = `
                <img src="${product.thumbnail}" alt="${product.title}" />
                <p>${product.title}</p>
                <p>$${product.price}
            `
            ;
            
            productBtn.addEventListener("click", () => {
                const cartProduct = {
                    title: product.title,
                    thumbnail: product.thumbnail,
                    price: product.price
                };
                cart.unshift(cartProduct);
                localStorage.setItem("cart", JSON.stringify(cart));
            });

            div.appendChild(productBtn);
            products.appendChild(div);
        });
    } catch (error) {
        console.error("Error fetching products:", error);
    }
};

window.addEventListener("DOMContentLoaded", getAllProducts);
productBtn.addEventListener("click", () => {
    const cartProduct = {
        title: product.title,
        thumbnail: product.thumbnail,
        price: product.price
    };
    
    // Play sound
    const sound = document.getElementById("add-sound");
    sound.currentTime = 0;
    sound.play();

    // Visual effect
    productBtn.classList.add("clicked");
    setTimeout(() => productBtn.classList.remove("clicked"), 300); // Remove after animation

    cart.unshift(cartProduct);
    localStorage.setItem("cart", JSON.stringify(cart));
});
