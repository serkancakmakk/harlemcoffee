document.addEventListener("DOMContentLoaded",function(){var e=document.querySelector("#search-input"),t=document.querySelectorAll("#productTableBody tr");e.addEventListener("input",function(){var n=e.value.trim().toLowerCase();t.forEach(function(e){e.textContent.trim().toLowerCase().includes(n)?e.style.display="":e.style.display="none"})})});
// //
//minify
//    document.addEventListener('DOMContentLoaded', function() {
//        // arama kutusunu ve tablodaki satırları seç
//        var searchInput = document.querySelector('#search-input');
//        var rows = document.querySelectorAll('#productTableBody tr');
       
//        // filtrelemeyi gerçekleştir
//        searchInput.addEventListener('input', function() {
//            // metni küçük harfe çevir
//            var searchText = searchInput.value.trim().toLowerCase();
           
//            // satırı kontrol et
//            rows.forEach(function(row) {
//                // satır içeriği
//                var rowData = row.textContent.trim().toLowerCase();
               
//                // satır aranan metni içeriyorsa göster
//                // Aksi halde satırı gizle
//                if (rowData.includes(searchText)) {
//                    row.style.display = '';
//                } else {
//                    row.style.display = 'none';
//                }
//            });
//        });
//    });