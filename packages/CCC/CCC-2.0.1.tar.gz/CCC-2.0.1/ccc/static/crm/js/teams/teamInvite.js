const teamInvite = new Vue({
    el: '#teamInvite',
    delimiters: ["[[", "]]"],
    data: {
        teams: [
            {
                id: 1,
                img: "static/images/images.jpeg",
                date: '8/2018',
                title: "Learn how to dance",
                description: "Burton Industries marketing - dedicated team for client’s campaigns.",
                name: "Sasha Burton",
                msg: "invited you to her team",
            },
			{
                id: 2,
                img: "static/images/images.jpeg",
                date: '8/2018',
                title: "Testing links",
                description: "This team is created just for testing our product’s functionality.",
                name: "George Kvasnikov",
                msg: "invited you to his team",
            },
			
			
		]
	}
});
