<template>
  <div class="field">
    <label class="label" v-if="label"> {{ label }}</label>

    <div class="control">
      <div class="select is-primary is-rounded">
        <select
          :value="modelValue"
          class="select is-rounded"
          v-bind="$attrs"
          @change="$emit('update:modelValue', $event.target.value)"
        >
          <option
            v-for="option in options"
            :value="option"
            :key="option"
            :selected="option === modelValue"
          >
            {{ option }}
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
    modelValue: {
      type: [String, Number],
      default: "",
    },
    options: {
      type: Array,
      required: true,
    },
  },
};
</script>
