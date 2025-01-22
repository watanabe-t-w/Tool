function onClickSearch() {
    let zip = document.getElementById("Postcode").value;
    zip = zip.replace(/\D/g, '');
    if(!zip.match(/\d{7}/)) {
      alert("郵便番号の入力に誤りがあります");
      return;
    }
    const hit = zipcode.filter(zc => zc.code === zip);
    if (hit.length === 0) {
      alert("該当の住所はありませんでした");
      return;
    }
    let csvAddr = document.getElementById("csvAddress");
    csvAddr.value = hit[0].pref + hit[0].addr;
  }
