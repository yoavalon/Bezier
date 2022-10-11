d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.W, Length.short)

d.end()
