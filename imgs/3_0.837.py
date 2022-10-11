d = DslBezier()

d.position_pen(0,3)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.W, Orient.left, Length.long, Radius.low)
d.curve(Direction.SW, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.W, Length.medium)

d.end()
