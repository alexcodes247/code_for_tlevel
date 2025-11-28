
document.getElementById("submit").addEventListener("click", BreedImage);

async function BreedImage() {
  const breed = document.getElementById("type").value;
  const sub = document.getElementById("subtype").value;

  const imageUrl = sub
    ? `https://dog.ceo/api/breed/${breed}/${sub}/images/random`
    : `https://dog.ceo/api/breed/${breed}/images/random`;

  try {
    const imgResponse = await fetch(imageUrl);
    const imgData = await imgResponse.json();

    const pretty = sub ? `${sub} ${breed}` : breed;

    document.getElementById("weather").innerHTML = `
      <h1>${pretty}</h1>
      <img src="${imgData.message}" alt="${pretty}">
    `;
  } catch (err) {
    console.error(err);
  }
}

async function loadBreeds() {
  const select = document.getElementById("type");

  try {
    const response = await fetch("https://dog.ceo/api/breeds/list/all");
    const data = await response.json();

    window.breedList = data.message;

    const breeds = Object.keys(data.message);

    breeds.forEach(breed => {
      const option = document.createElement("option");
      option.value = breed;
      option.textContent = breed;
      select.appendChild(option);
    });

    loadSubBreeds(select.value);

  } catch (err) {
    console.error(err);
  }
}

function loadSubBreeds(breed) {
  const subSelect = document.getElementById("subtype");
  subSelect.innerHTML = "";

  const subs = window.breedList[breed];

  if (subs.length === 0) {
    subSelect.style.display = "none";
    subSelect.value = "";
  } else {
    subSelect.style.display = "inline-block";

    subs.forEach(sub => {
      const option = document.createElement("option");
      option.value = sub;
      option.textContent = sub;
      subSelect.appendChild(option);
    });
  }
}

document.getElementById("type").addEventListener("change", (e) => {
  loadSubBreeds(e.target.value);
});

loadBreeds();
