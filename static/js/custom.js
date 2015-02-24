// Add social icon classes to links
function updateLinkClass(links) {
	for(var i=0; i < links.length; i++) {
		link = $(links[i])
		linkName = link.attr('data-name').toLowerCase();
		console.log(linkName)
		if(linkName.search('facebook') !== -1) {
			link.addClass('facebook');
		} else if(linkName.search('twitter') !== -1) {
			link.addClass('twitter');
		} else if(linkName.search('linkedin') !== -1) {
			link.addClass('linkedin');
		} else if(linkName.search('quora') !== -1) {
			link.addClass('quora');
		} else if(linkName.search('instagram') !== -1) {
			link.addClass('instagram');
		} else if(linkName.search('github') !== -1) {
			link.addClass('github');
		} else if(linkName.search('blog') !== -1) {
			link.addClass('blog');
		} else if(linkName.search('website') !== -1) {
			link.addClass('blog');
		}
	}
}
