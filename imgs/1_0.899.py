d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.NW, Length.short)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.SW, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)

d.end()
