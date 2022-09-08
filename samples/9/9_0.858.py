d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.short)

d.end()
