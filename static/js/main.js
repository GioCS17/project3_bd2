Vue.options.delimiters = ['{[{', '}]}'];
var v = new Vue({
    el:'#app',
    data:{
        selectedFiles:[],
        knn:0,
        msg:[],
        spinner : false,
        spinner2 : false
    },
    methods: {
        clearSearchField(){
        },
        upSelectedFiles(event){
            this.selectedFiles=event.target.files;
        },
        async upLoadAll(){
            this.spinner2 = true
            const fd = new FormData();
            fd.append('file',this.selectedFiles[0])
            fd.append("text", this.knn);
            //fd.append('text',this.knn2)
            var url='http://127.0.0.1:5000/upload';
            await axios.post(url,fd)
            .then(function(res){
                if(res.status==201)
                    console.log("exitos")
                })
            .catch(function(err){
                console.log(err)
            })
            .then(function(){
                console.log("Finish")
            })
            this.spinner2 = false
        },
        async search(to_search) {
            console.log("consulta entro a search")
            this.spinner = true
            const path = 'http://localhost:5000/tweets/' + to_search;
            await axios.get(path)
                .then((res) => {
                this.msg = res.data;
                this.msg.sort((a,b) => (a.score < b.score) ? 1 : ((b.score < a.score) ? -1 : 0));
            })
            .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
            });
            this.spinner = false
        }
    },
    computed: {
    },

});