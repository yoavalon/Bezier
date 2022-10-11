d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.right, Length.long, Radius.low)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.NE, Length.medium)

d.end()
