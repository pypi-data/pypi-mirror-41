Vue.component('accordion', {
    props: ['elementID'],
    data () {
        return {

        }
    },
    template: `
        <ul :id="elementID" uk-accordion>
          <slot></slot>
        </ul>
    `
})

Vue.component('questions', {
    data () {
        return {

        }
    },
    delimiters: ["[[", "]]"],
    props: ['questions', 'parentquestion', 'parentanswer', 'is_root'],
    methods: {
        onEvent (event, parentanswer, parentquestion) {
            let new_order = []
            this.questions_.forEach((value, index) => {
                new_order.push({order: index, id: value.id})
            })
            let payload = {
                order: new_order, parent_answer: parentanswer, parent_question: parentquestion
            }
            HTTPClient.post('/api/marketing/surveys/questions/re-sort/', payload)
                .then(resp => console.log('Sort Logged'))
        },
        addFollowupToAnswerChoice (question_index, option_index) {
            //Todo: cant add follow up to answer from the tree view
            // this.$emit('add-follow-up-to-answer', {question_index: question_index, option_index: option_index})
        },
        deleteQuestion (question) {
            this.$emit('delete-question', question)
        },
        openEditQuestion (question) {
            this.$emit('open-edit-question', question)
        },
        toggleAccordion (index, element_id) {
            UIkit.accordion('#' + element_id).toggle(index, true);
        },
        getComponentData () {
            return {
                props: {
                    elementID: this.elementID
                }
            }
        }
    },
    computed: {
        questions_: {
            get () {
                return this.questions
            },
            set (newValue) {
                this.$emit('update-questions', newValue)
            }
        },
        elementID () {
            return this.is_root ? 'question-accordion' : 'question-accordion-' + this.parentanswer || (this.parentquestion + '-q')
        }
    },
    template: `
        <draggable :list="questions_"  element="accordion" :component-data="getComponentData()" @sort="onEvent($event, parentanswer, parentquestion)">
          <li class="tree-node-inner question-node" :key="index" v-for="(data, index) in questions_">
            <a href="#" class="uk-accordion-title question-accordion-title uk-position-relative">
              <div class="question-accordion-actions">
                  <a class="survey-tree-edit-icon uk-icon-button" data-uk-icon="pencil" @click.prevent.stop="$emit('open-edit-question', data)"></a>
                  <a class="survey-tree-delete-icon uk-icon-button" data-uk-icon="trash" @click.prevent.stop="$emit('delete-question', data)"></a>
                  <a class="survey-tree-toggle-icon uk-icon-button" data-uk-icon="expand" @click.stop.prevent="toggleAccordion(index, elementID)" href="#" v-if="data.answer_choices.length || data.children.length"></a>
              </div>
              <span class="survey-tree-question">
                <span data-uk-icon="question"></span>  [[data.question]] ([[data.question_type === 'mcq' ? 'Multiple Choice' : 'Text']])
              </span>
            </a>
            <div class="uk-accordion-content">
              <ul class="survey-question-option-list" v-if="data.answer_choices.length">
                <li v-for="(option, key) in data.answer_choices">
                  <div class="survey-option">
                    If Chosen Option: <span>[[option.answer]]</span>  <span v-if="option.should_halt" data-uk-tooltip="Halt survey if selected" data-uk-icon="ban" class="uk-text-danger"></span>
                  </div>
                  <questions 
                    v-if="option.children.length" 
                    :questions="option.children"
                    :parentanswer="option.id"
                    @delete-question="deleteQuestion" 
                    @open-edit-question="openEditQuestion"
                    @add-follow-up-to-answer="addFollowupToAnswerChoice"
                    :survey="data.survey_id">
                  </questions>
                </li>
              </ul>
              <div v-if="data.children.length">
                <h4 class="uk-h4 question-list-title">Follow up questions</h4>
                <questions 
                    v-if="data.children.length" 
                    :questions="data.children"
                    :parentquestion="data.id"
                    @delete-question="deleteQuestion" 
                    @open-edit-question="openEditQuestion"
                    @add-follow-up-to-answer="addFollowupToAnswerChoice"
                    :survey="data.survey_id">
                </questions>
              </div>
            </div>
          </li>
        </draggable>
    `,
    mounted () {
    }
})

const survey = new Vue({
    el: '#survey',
    delimiters: ["[[", "]]"],
    mixins: [],
    components: {
    },
    data: {
        survey_id: survey_id,
        surveyQuestions: [],
        surveyQuestionsLevels: [],
        currentQuestion: {
            id: null,
            delay: 0,
            survey: null,
            survey_id: 0,
            question: null,
            question_type: 'mcq',
            contact_mapping: null,
            in_response_of_question: [],
            in_response_of: [],
            answer_choices: [],
            parent_question: null,
            parent_answer: null,
            question_type_name: null,
            delay_value: 0,
            schedular_step: 0,
        },
        error: {},
        surveyQuestionOptions: {
            schedular_step: [],
            contact_mapping: [],
            question_types: []
        },
        // For computed property
        question_to_answer: {
            question: null,
            option: null
        },
        tableView: Boolean(parseInt(window.localStorage.getItem('questionsTableView')) || 1),
        questionsLevelLoading: false,
        questionsLoading: false
    },
    mounted() {
        this.getQuestionsForAllViews()
        this.getQuestionOptions();
    },
    watch: {
        tableView (newVal) {
            window.localStorage.setItem('questionsTableView', newVal ? '1' : '0')
        }
    },
    computed: {
        getCurrentFollowUpName () {
            let index = this.surveyQuestions.findIndex(item => item.id === this.currentQuestion.parent_question)
            return this.surveyQuestions[index] ? this.surveyQuestions[index].question : ''
        },
        getCurrentAnswerFollowUpName () {
            let answer = this.question_to_answer.answer
            let question = this.question_to_answer.question
            return this.surveyQuestions[question].question + '(' + this.surveyQuestions[question].answer_choices[answer].answer + ')'
        }
    },
    methods: {
        addQuestion: function () {
            this.error = {}
            /*Add new question. Posting to API*/
            this.saveQuestion()
                .then(response => {
                    UIkit.modal('#add-survey-question-modal').hide();
                    this.resetCurrentQuestionFields();
                    this.getQuestionsForAllViews()
                })
                .catch(err => {
                    this.error = err.response.data
                    console.log(err);
                });
        },
        editQuestion () {
            this.error = {}
            this.updateQuestion()
                .then(response => {
                    UIkit.modal('#edit-survey-question-modal').hide();
                    this.resetCurrentQuestionFields();
                    this.getQuestionsByLevel()

                })
                .catch(err => {
                    this.error = err.response.data
                    console.log(err);
                })
        },
        saveQuestion () {
            const urlAddQuestion = '/api/marketing/surveys/' + parseInt(this.$el.getAttribute('data-survey')) + '/add_question/';
            this.currentQuestion.survey_id = parseInt(this.$el.getAttribute('data-survey'));
            return HTTPClient.post(urlAddQuestion, this.currentQuestion)
        },
        updateQuestion: function () {

            let urlUpdateQuestion = '/api/marketing/surveys/questions/' + this.currentQuestion.id + '/'

            return HTTPClient.patch(urlUpdateQuestion, this.currentQuestion)
        },
        isQuestionTextBasedResponse: function () {
            /*Returns boolean. True if the type of currenQuestion is Text based Response*/
            return this.currentQuestion.question_type === 'text';

        },

        isQuestionMultipleChoice: function () {
            /*Returns boolean. True if the type of currenQuestion is multiple choice*/
            return this.currentQuestion.question_type === 'mcq';

        },

        getQuestionOptions: function () {
            /*Get all available question options*/

            const url_question_options = '/api/marketing/surveys/questions/options/';

            HTTPClient.get(url_question_options)
                .then(response => {
                    this.surveyQuestionOptions = response.data;
                })
                .catch(err => {
                    console.log(err);
                });
        },

        getQuestions: function () {
            /*Get all question for the survey instance.*/
            const url_questions_list = '/api/marketing/surveys/' + parseInt(this.$el.getAttribute('data-survey')) + '/questions/';
            this.questionsLoading = true

            HTTPClient.get(url_questions_list)
                .then(response => {
                    this.surveyQuestions = response.data;
                    this.questionsLoading = false
                })
                .catch(err => {
                    console.log(err);
                    this.questionsLoading = false
                });
        },

        getQuestionsByLevel () {
            const url_questions_list = '/api/marketing/surveys/' + parseInt(this.$el.getAttribute('data-survey')) + '/questions/?level=true';
            this.questionsLevelLoading = true
            HTTPClient.get(url_questions_list)
                .then(response => {
                    this.surveyQuestionsLevels = response.data;
                    this.questionsLevelLoading = false
                })
                .catch(err => {
                    console.log(err);
                    this.questionsLevelLoading = false
                });
        },

        getQuestionsForAllViews () {
            this.getQuestions()
            this.getQuestionsByLevel()
        },

        deleteQuestion (index) {
            // Index could be the question object or the index in the surveyQuestions list
            UIkit.modal.confirm('Are you sure you want to delete this question ?')
                .then(r => {
                    const question = typeof index === 'object' ? index.id : this.surveyQuestions[index].id
                    HTTPClient.delete('/api/marketing/surveys/questions/' +  question + '/')
                        .then(resp => {
                            this.getQuestionsForAllViews()
                        })
                })
        },

        openEditQuestion(index) {
            typeof index === 'object' ? this.currentQuestion = index : this.currentQuestion = this.surveyQuestions[index]
            UIkit.modal('#edit-survey-question-modal').show()
        },

        openAddQuestion(callback=null) {
            this.resetCurrentQuestionFields()
            callback && typeof callback === 'function' ? callback() : null // some values to prefill before display modal
            UIkit.modal('#add-survey-question-modal').show()
        },

        addOptionToQuestion() {
            this.currentQuestion.answer_choices.push({question_id: parseInt(this.$el.getAttribute('data-survey')), answer: '', should_halt: false})
        },

        removeOptionFromQuestion(key) {
            HTTPClient.delete('/api/marketing/surveys/questions/answer-options/' + this.currentQuestion.answer_choices[key].id)
                .then(resp => {
                    this.currentQuestion.answer_choices.splice(key, 1)
                })
        },

        addFollowUpQuestion (action) {
            let method = null
            if (action === 'create') {
                method = this.saveQuestion
            }
            else {
                method = this.updateQuestion
            }
            this.error = {}
            method ()
                .then(response => {
                    action === 'create' ? this.getQuestionsForAllViews() : null
                    this.openAddQuestion(() => this.currentQuestion.parent_question = response.data.id)
                })
                .catch(error => {
                    this.error = error.response.data
                })
        },
        addFollowupToAnswerChoice (question_index, answer_index) {
            this.resetCurrentQuestionFields()
            this.currentQuestion.parent_answer = this.surveyQuestions[question_index].answer_choices[answer_index].id;
            this.question_to_answer = {
                question: question_index,
                answer: answer_index
            }
            UIkit.modal('#add-survey-question-modal').show();
        },
        resetCurrentQuestionFields() {
            this.currentQuestion = {
                id: null,
                delay: 0,
                survey: null,
                survey_id: 0,
                question: null,
                question_type: 'mcq',
                contact_mapping: null,
                in_response_of_question: [],
                in_response_of: [],
                parent_question: null,
                answer_choices: [],
                question_type_name: null,

                schedular_step: 0,
                delay_value: 0
            }
        },
        updateQuestionList (newQuestions) {
            this.surveyQuestions = newQuestions
        }
    },

})
