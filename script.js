function updateRemoveButtons() {
    const removeButtons = document.querySelectorAll('.criterio-row .btn-danger')
    if (document.querySelectorAll('.criterio-row').length <= 3) {
        removeButtons.forEach(button => button.disable = true)
    } else {
        removeButtons.forEach(button => button.disable = false)
    }
}


async function submitForm() {
    const criterioInputs = document.getElementsByClassName('criterio')
    const criterios = [];
    for (let i = 0; i < criterioInputs.length; i++) {
        if (criterioInputs[i].value) {
            criterios.push(criterioInputs[i].value)
        }
    }
    if (criterios.length < 3) {
        alert('Por favor, preencha pelo menos três campos!')
        return
    }

    const data = {
        criterios: criterios
    }

    try {
        const response = await fetch('http://localhost:5000/redacao', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })

        const result = await response.json()

        const responseDiv = document.getElementById('response')
        if (result) {
            const redacao = `${result.join('')}`
            responseDiv.innerHTML = redacao
        } else {
            responseDiv.innerHTML = `<p>Erro: ${result.Erro}</p>`
        }
        responseDiv.style.display = 'block'
    } catch (error) {
        const responseDiv = document.getElementById('response')
        responseDiv.innerHTML = `<p>Erro: ${error.message}</p>`
        responseDiv.style.display = 'block'
    }
}

document.addEventListener('DOMContentLoaded', updateRemoveButtons)