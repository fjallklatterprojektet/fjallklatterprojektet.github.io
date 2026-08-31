
function removeDiacritics(string)
{
  return string.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}

function filterPostList(filterText)
{
  const filters = removeDiacritics(filterText).toUpperCase().split(" ");
  const ul = document.getElementById("post_list");

  for (const li of ul.getElementsByTagName("li"))
  {
    p = li.getElementsByTagName("p")[0];
    const text = removeDiacritics((p.textContent || p.innerText).toUpperCase());

    var showListItem = true;
    for (const filter of filters)
    {
      if (text.indexOf(filter) == -1)
      {
        showListItem = false;
        break;
      }
    }
    li.style.display = showListItem ? "" : "none";
  }
}

function addTagToSearchBox(tag)
{
  input = document.getElementById("search_input");
  input.value = removeDiacritics(tag);
  filterPostList(tag);
}

function addTagValueFromQueryStringToSearchBox()
{
  let params = new URLSearchParams(window.location.search);
  if (params.has("tag"))
  {
    addTagToSearchBox(params.get("tag"));
  }
}
addTagValueFromQueryStringToSearchBox();
