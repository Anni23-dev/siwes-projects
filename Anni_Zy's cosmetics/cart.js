let cart = JSON.parse(localStorage.getItem("cart")) || [];
const cartBody = document.getElementById("cartBody");

function renderCart() {
    cartBody.innerHTML = "";

    const productMap = new Map();

    // Group products by title and count quantities
    cart.forEach(product => {
        if (productMap.has(product.title)) {
            productMap.get(product.title).quantity += 1;
        } else {
            productMap.set(product.title, { ...product, quantity: 1 });
        }
    });

    // Convert map to array
    const groupedCart = Array.from(productMap.values());

    // Render each row
    groupedCart.forEach((item, index) => {
        const tr = document.createElement("tr");
        tr.innerHTML = `
            <td>
                <img src="${item.thumbnail}" alt="${item.title}" />
                <p>${item.title}</p>
            </td>
            <td>$${item.price * item.quantity}</td>
            <td>
                <button class="quantity-btn" data-index="${index}" data-action="decrement">−</button>
                <span class="quantity">${item.quantity}</span>
                <button class="quantity-btn" data-index="${index}" data-action="increment">+</button>
            </td>
        `;
        cartBody.appendChild(tr);
    });

    attachButtonHandlers(groupedCart);
}

function attachButtonHandlers(groupedCart) {
    const buttons = document.querySelectorAll(".quantity-btn");

    buttons.forEach(button => {
        const index = parseInt(button.getAttribute("data-index"));
        const action = button.getAttribute("data-action");
        const product = groupedCart[index];

        button.addEventListener("click", () => {
            const cartIndex = cart.findIndex(p => p.title === product.title);
            if (action === "increment") {
                cart.push(product);
            } else if (action === "decrement") {
                const removeIndex = cart.findIndex(p => p.title === product.title);
                if (removeIndex !== -1) {
                    cart.splice(removeIndex, 1);
                }
            }

            localStorage.setItem("cart", JSON.stringify(cart));
            renderCart();
        });
    });
}

document.addEventListener("DOMContentLoaded", renderCart);
let total = 0;
groupedCart.forEach(item => {
    total += item.price * item.quantity;
});
document.getElementById("total").textContent = `Total: $${total}`;
