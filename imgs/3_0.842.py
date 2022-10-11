d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.S, Length.medium)

d.end()
