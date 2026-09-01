
function expandTags()
{
  document.getElementById('expandable_tags').style.display = 'inline';
  document.getElementById("expand_tags_button").style.display = 'none';
}

function setupExpandableTags()
{
  document.getElementById("expand_tags_button").style.display = "inline-block";
  document.getElementById("expandable_tags").style.display = "none";
}
setupExpandableTags();
