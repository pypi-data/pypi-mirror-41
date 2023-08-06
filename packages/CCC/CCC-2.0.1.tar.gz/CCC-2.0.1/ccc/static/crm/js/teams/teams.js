var count = 0;

const Teams = new Vue({
    el: '#Teams',
    delimiters: ["[[", "]]"],
    data: {
        teams: [
            {
                id: 1,
                img: "/../static/crm/images/images.jpeg",
                date: '8/2018',
                location: 'Los Angeles',
                email: "sasha.burton@burton.io",
                title: "Learn how to dance",
                description: "Burton Industries marketing - dedicated team for client’s campaigns.",
                teamname: 'Sasha’s team',
                name: "Sasha Burton",
                
            },
			{
                id: 2,
                img: "/../static/crm/images/images.jpeg",
                date: '8/2018',
                location: 'Los Angeles',
                email: "g.kvasnikov@fantasy.io",
                title: "Testing links",
                description: "This team is created just for testing our product’s functionality.",
                teamname: 'George’s team',
                name: "George Kvasnikov",
            },
			{
                id: 3,
                img: "/../static/crm/images/images.jpeg",
                date: '8/2018',
                location: 'Los Angeles',
                email: "tobias@epamsystems.com",
                title: "Test campaign",
                description: "Epam Systems marketing team - dedicated team for Epam’s ad campaigns.",
                teamname: 'Tobias’s team',
                name: "Tobias Van Schneider",
            },
            {
                id: 4,
                img: "/../static/crm/images/images.jpeg",
                date: '8/2018',
                location: 'Los Angeles',
                email: "sasha.burton@burton.io",
                title: "Learn how to dance",
                description: "Burton Industries marketing - dedicated team for client’s campaigns.",
                teamname: 'Sasha’s team',
                name: "Sasha Burton",

            },
			{
                id: 5,
                img: "/../static/crm/images/images.jpeg",
                date: '8/2018',
                location: 'Los Angeles',
                email: "g.kvasnikov@fantasy.io",
                title: "Testing links",
                description: "This team is created just for testing our product’s functionality.",
                teamname: 'George’s team',
                name: "George Kvasnikov",
            },
			{
                id: 6,
                img: "/../static/crm/images/images.jpeg",
                date: '8/2018',
                location: 'Los Angeles',
                email: "tobias@epamsystems.com",
                title: "Test campaign",
                description: "Epam Systems marketing team - dedicated team for Epam’s ad campaigns.",
                teamname: 'Tobias’s team',
                name: "Tobias Van Schneider",
            },
			
		],
		busy: false
	},
	methods: {
	    loadMore: function() {
	    this.busy = true;
	    setTimeout(() => {
	    for (var i = 0, j=3; i<j; i++){
	        this.teams.push({name: count++ });
	        }
	         this.busy = false;
	       }, 1000);
	    }
	}
});
