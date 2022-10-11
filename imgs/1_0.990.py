d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.curve(Direction.S, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.NE, Length.medium)

d.end()
