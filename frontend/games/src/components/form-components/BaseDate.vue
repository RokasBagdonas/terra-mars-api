<template>
  <div class="field">
    <label class="label" v-if="label">{{ label }}</label>
    <div class="control">
      <input
        type="date"
        class="date"
        :value="pickedDate.toJSON().substring(0,10)"
        v-bind="$attrs"
        @input="updateDate"
      />
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
    modelValue: {
      type: Date,
      default: new Date(),
    },
  },
  data() {
    return {
      pickedDate: this.modelValue,
    };
  },
  methods: {
    updateDate(e) {
      this.pickedDate = new Date(e.target.value);
      this.$emit("update:modelValue", this.pickedDate);
    },
  },
};
</script>
