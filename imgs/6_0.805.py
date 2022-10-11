d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NW, Length.long)
d.position_pen(2,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.medium)

d.end()
