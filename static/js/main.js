Vue.options.delimiters = ['{[{', '}]}'];
var v = new Vue({
    el:'#app',
    data:{
        selectedFiles:[],
        knn:0,
        msg:[],
        spinner : false,
        spinner2 : false,
        images_eucl:[],
        images_manh:[],
        images_rtree:[]
    },
    methods: {
        clearSearchField(){
        },
        upSelectedFiles(event){
            this.selectedFiles=event.target.files;
        },
        buildRTree(){
           var url='http://127.0.0.1:5000/buildRtree';
           axios.get(url)
                .then(response => (console.log("Rtree created")))

        },
        async upLoadAll(){
            this.spinner2 = true
            const fd = new FormData();
            fd.append('file',this.selectedFiles[0])
            if(this.knn==0)
                this.knn=2
            fd.append("text", this.knn);
            var url='http://127.0.0.1:5000/upload';
            await axios.post(url,fd)
            .then(res=>{
                    if(res.data.status==201)
                        console.log("exitos")

                    for(i=0;i<this.knn;i++)
                        this.images_eucl[i]="data:image.jpg;base64, "+res.data.data_images[i]
                    for(i=this.knn,j=0;i<2*this.knn;i++,j++)
                        this.images_manh[j]="data:image.jpg;base64, "+res.data.data_images[i]
                    for(i=2*this.knn,j=0;i<3*this.knn;i++,j++)
                        this.images_rtree[j]="data:image.jpg;base64, "+res.data.data_images[i]
                })
            .catch(function(err){
                console.log(err)
            })
            .then(function(){
                console.log("Finish")
            })
            this.spinner2 = false
        },
    },
    computed: {
    },

});