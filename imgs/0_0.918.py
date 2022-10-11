d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.SW, Orient.left, Length.long, Radius.high)
d.position_pen(1,1)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.SW, Length.medium)

d.end()
