function onEdit(e) {
  const sheet = e.source.getActiveSheet();
  const sheetName = sheet.getName();
  const DATE_FORMAT = "dd-MM-yyyy";
  
  if (sheetName === "Neetcode 150[ANKI]" || sheetName === "Foundation") { 
    const range = e.range;
    const row = range.getRow();
    const col = range.getColumn();

    // Get column indices from headers (row 1)
    const headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
    const lastReviewedCol = headers.indexOf("Last Reviewed") + 1;
    const nextReviewCol = headers.indexOf("Next Review") + 1;
    const intervalCol = headers.indexOf("Interval") + 1;
    const easeCol = headers.indexOf("Ease") + 1;
    const scoreCol = headers.indexOf("Score") + 1;
    const reviewsCol = headers.indexOf("Reviews") + 1;
    const historyCol = headers.indexOf("History") + 1;

    // Check if the edited cell is in the "Score" column and not the header row
    if (col === scoreCol && row > 1) {
      const score = sheet.getRange(row, scoreCol);
      const scoreValue = score.getValue();

      // Skip processing if the score is empty
      if (scoreValue === "") return;

      const lastReviewed = sheet.getRange(row, lastReviewedCol);
      const interval = sheet.getRange(row, intervalCol);
      const ease = sheet.getRange(row, easeCol);
      const reviewCount = sheet.getRange(row, reviewsCol);
      const history = sheet.getRange(row, historyCol);

      // Initialize default values if empty
      if (interval.isBlank()) interval.setValue(1);
      if (ease.isBlank()) ease.setValue(2.5);
      if (reviewCount.isBlank()) reviewCount.setValue(0);
      if (history.isBlank()) history.setValue("");

      // Update Last Reviewed Date
      lastReviewed.setValue(Utilities.formatDate(new Date(), Session.getScriptTimeZone(), DATE_FORMAT));

      // Update Interval and Ease Factor based on score
      let newInterval = interval.getValue();
      let newEase = ease.getValue();
      
      if (scoreValue === 0 || scoreValue === -1) {
        newInterval = 1;
        newEase -= 0.2;
      } else if (scoreValue === 1 || scoreValue === 11) {
        newInterval *= 1.2;
        newEase -= 0.15;
      } else if (scoreValue === 2 || scoreValue === 22) {
        newInterval *= newEase;
      } else if (scoreValue === 3 || scoreValue === 33) {
        newInterval *= newEase * 1.3;
        newEase += 0.15;
      }

      interval.setValue(newInterval);
      ease.setValue(newEase);

      // Update Review Count
      reviewCount.setValue(reviewCount.getValue() + 1);

      // Update History
      const formattedDate = Utilities.formatDate(new Date(), Session.getScriptTimeZone(), DATE_FORMAT);
      const newHistoryEntry = `${formattedDate} (${scoreValue})`;
      history.setValue(history.getValue() ? `${history.getValue()} ${newHistoryEntry}` : newHistoryEntry);

      // Update Next Review Date
      const nextReviewDate = new Date();
      nextReviewDate.setDate(nextReviewDate.getDate() + newInterval);
      sheet.getRange(row, nextReviewCol).setValue(Utilities.formatDate(nextReviewDate, Session.getScriptTimeZone(), DATE_FORMAT));
    }
  }
}
