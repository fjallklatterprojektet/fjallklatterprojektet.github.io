
function filterPostList(filterText) {
  const filters = filterText.toUpperCase().split(" ");
  const ul = document.getElementById("post_list");

  for (const li of ul.getElementsByTagName("li"))
  {
    p = li.getElementsByTagName("p")[0];
    const text = p.textContent || p.innerText;
    var showListItem = true;
    for (const filter of filters)
    {
      if (text.toUpperCase().indexOf(filter) == -1)
      {
        showListItem = false;
        break;
      }
    }
    li.style.display = showListItem ? "" : "none";
  }
}

function addTagToSearchBox(tag) {
  input = document.getElementById("search_input");
  input.value = tag;
  filterPostList(tag);
}
