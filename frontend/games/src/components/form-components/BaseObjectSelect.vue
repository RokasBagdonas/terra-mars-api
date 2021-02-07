<template>
  <div class="field">
    <label class="label" v-if="label">{{ label }}</label>

    <div class="control">
      <div class="select is-primary">
        <select v-model="selected" v-bind="$attrs" @change="setObject">
          <option
            v-for="(option, index) in options"
            :value="index"
            :key="option"
            :selected="options[0][displayProp]"
          >
            {{ option[displayProp] }}
          </option>
        </select>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  props: {
    label: {
      type: String,
      default: "",
    },
    displayProp: {
      type: String,
      default: "",
    },
    modelValue: {
      type: Object,
      default: null,
    },
    options: {
      type: Array,
      required: true,
    },
  },
  setup() {
    return {
      selected: {},
    };
  },
  methods: {
    setObject(e) {
      console.log(e.target.value);
      let newValue = this.options[e.target.value];
      this.$emit("update:modelValue", newValue);
    },
  },
};
</script>
