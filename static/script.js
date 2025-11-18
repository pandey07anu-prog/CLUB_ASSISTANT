// ✅ Updated Universal Script for All Club Pages (Works with Dropdowns or Radio Buttons)

document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const output = document.getElementById("output");

  if (!form) {
    console.error("❌ No form found on this page.");
    return;
  }

  // 🧭 Detect which category page we’re on
  const currentPage = window.location.pathname.toLowerCase();
  let category = "";
  if (currentPage.includes("music")) category = "MUSIC";
  else if (currentPage.includes("art")) category = "ARTS";
  else if (currentPage.includes("sports")) category = "SPORTS";
  else if (currentPage.includes("coding")) category = "CODING";
  else category = "GENERAL";

  form.addEventListener("submit", async function (e) {
    e.preventDefault();

    // 🎯 Collect form data (dropdowns, radios, checkboxes, text)
    const formData = new FormData(form);
    const dataToSend = { category: category };

    // Extract values intelligently
    formData.forEach((value, key) => {
      if (!dataToSend[key]) dataToSend[key] = value;
    });

    // For debugging
    console.log("📤 Sending to backend:", dataToSend);

    try {
      const response = await fetch("/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(dataToSend),
      });

      const data = await response.json();
      console.log("✅ Response received:", data);

      // 🧾 Show output neatly
      output.innerHTML = "";
      if (data.clubs && data.clubs.length > 0) {
        data.clubs.forEach((club) => {
          output.innerHTML += `
            <div class="club-card">
              <h3>${club.Activity}</h3>
              <p><strong>Category:</strong> ${club.Category}</p>
              <p><strong>Details:</strong> ${club.Details}</p>
            </div>
          `;
        });
      } else {
        output.innerHTML = data.message || "No matching clubs found.";
      }
    } catch (error) {
      console.error("❌ Error:", error);
      alert("Failed to connect to server. Make sure Flask is running.");
    }
  });
});
