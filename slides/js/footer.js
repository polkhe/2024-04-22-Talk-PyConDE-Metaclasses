Reveal.addEventListener("ready", event => {
    const controls = document.querySelector("aside.controls")
    controls.innerHTML = (
        `
        <div class="hf-logo-wrapper">
            <img src="img/HelloFresh-Logo.png" alt="logo">
        </div>
        `
        + controls.innerHTML
    )    
})

