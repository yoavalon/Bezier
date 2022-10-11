d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NE, Orient.left, Length.long, Radius.low)
d.curve(Direction.W, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.NW, Length.long)

d.end()
